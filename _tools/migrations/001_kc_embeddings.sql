-- CEX Knowledge Card Embeddings
-- Run this in Supabase Dashboard > SQL Editor
-- https://supabase.com/dashboard/project/fuuguegkqnpzrrhwymgw/sql/new

-- 1. Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Knowledge Card embeddings table
CREATE TABLE IF NOT EXISTS kc_embeddings (
    id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    pillar TEXT,
    domain TEXT,
    title TEXT,
    tldr TEXT,
    tags TEXT[],
    feeds_kinds TEXT[],
    file_path TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    embedding vector(1536),  -- text-embedding-3-small dimensions
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Vector similarity index (IVFFlat for fast cosine search)
-- Note: IVFFlat needs rows to exist first; use HNSW for empty tables
CREATE INDEX IF NOT EXISTS kc_embeddings_hnsw_idx 
    ON kc_embeddings 
    USING hnsw (embedding vector_cosine_ops);

-- 4. Filter indexes
CREATE INDEX IF NOT EXISTS kc_embeddings_kind_idx ON kc_embeddings(kind);
CREATE INDEX IF NOT EXISTS kc_embeddings_domain_idx ON kc_embeddings(domain);
CREATE INDEX IF NOT EXISTS kc_embeddings_hash_idx ON kc_embeddings(content_hash);

-- 5. Search function: find KCs by vector similarity
CREATE OR REPLACE FUNCTION search_kcs(
    query_embedding vector(1536),
    match_count INT DEFAULT 5,
    filter_kind TEXT DEFAULT NULL,
    filter_domain TEXT DEFAULT NULL
)
RETURNS TABLE (
    id TEXT,
    kind TEXT,
    domain TEXT,
    title TEXT,
    tldr TEXT,
    tags TEXT[],
    feeds_kinds TEXT[],
    file_path TEXT,
    similarity FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        k.id, k.kind, k.domain, k.title, k.tldr, k.tags, k.feeds_kinds, k.file_path,
        1 - (k.embedding <=> query_embedding) AS similarity
    FROM kc_embeddings k
    WHERE (filter_kind IS NULL OR k.kind = filter_kind)
      AND (filter_domain IS NULL OR k.domain = filter_domain)
      AND k.embedding IS NOT NULL
    ORDER BY k.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;

-- 6. Upsert function (insert or update by content hash)
CREATE OR REPLACE FUNCTION upsert_kc(
    p_id TEXT,
    p_kind TEXT,
    p_pillar TEXT,
    p_domain TEXT,
    p_title TEXT,
    p_tldr TEXT,
    p_tags TEXT[],
    p_feeds_kinds TEXT[],
    p_file_path TEXT,
    p_content_hash TEXT,
    p_embedding vector(1536)
)
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO kc_embeddings (id, kind, pillar, domain, title, tldr, tags, feeds_kinds, file_path, content_hash, embedding, updated_at)
    VALUES (p_id, p_kind, p_pillar, p_domain, p_title, p_tldr, p_tags, p_feeds_kinds, p_file_path, p_content_hash, p_embedding, now())
    ON CONFLICT (id) DO UPDATE SET
        kind = EXCLUDED.kind,
        pillar = EXCLUDED.pillar,
        domain = EXCLUDED.domain,
        title = EXCLUDED.title,
        tldr = EXCLUDED.tldr,
        tags = EXCLUDED.tags,
        feeds_kinds = EXCLUDED.feeds_kinds,
        file_path = EXCLUDED.file_path,
        content_hash = EXCLUDED.content_hash,
        embedding = EXCLUDED.embedding,
        updated_at = now();
END;
$$;

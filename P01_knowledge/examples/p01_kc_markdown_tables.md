---  
id: p01_kc_markdown_tables  
kind: knowledge_card  
pillar: P01  
title: Markdown Tables Syntax and Best Practices  
version: "1.0.0"  
created: "2023-10-05"  
updated: "2023-10-05"  
author: "knowledge-team"  
domain: "markdown"  
quality: null  
tags: [markdown, tables, syntax, formatting]  
tldr: "Markdown tables use pipes and dashes to format structured data."  
when_to_use: "When formatting structured data in markdown documents."  
keywords: [markdown, tables, syntax]  
long_tails:  
  - "How to align columns in markdown tables?"  
  - "What is the syntax for markdown tables?"  
axioms:  
  - "ALWAYS use pipes to separate columns"  
  - "NEVER omit the header separator row"  
linked_artifacts:  
  primary: "https://commonmark.org/help/"  
---  
## Syntax  
Markdown tables use pipes `|` to separate columns and dashes `-` to define headers.  
### Basic Structure  
| Header 1 | Header 2 |  
|----------|----------|  
| Row 1    | Data     |  
| Row 2    | Data     |  

### Alignment  
Colons `:` control alignment:  
- `:--:` centers text  
- `:---` left-aligns  
- `---:` right-aligns  

## Best Practices  
- Always include the header separator row  
- Use consistent spacing between pipes  
- Avoid trailing spaces after pipes  
- Tables must have at least two rows: header + separator  

## Limitations  
- No support for merged cells  
- Complex formatting requires HTML fallback
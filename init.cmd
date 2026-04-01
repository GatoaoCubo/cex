@echo off
:: CEX INIT — The simplest possible entry point
:: User just double-clicks this or types: cex init
:: Detects state and does the right thing.

set CEX_ROOT=%~dp0
cd /d "%CEX_ROOT%"

if exist ".cex\brand\.bootstrapped" (
    echo.
    echo   CEX ja esta configurado para sua marca.
    echo.
    python _tools/cex_bootstrap.py --status
    echo.
    echo   Para reconfigurar: python _tools/cex_bootstrap.py --reset
    echo   Para editar:       .cex\brand\brand_config.yaml
    echo   Para iniciar:      boot\cex.cmd
    echo.
    pause
) else (
    echo.
    echo   ============================================================
    echo     BEM-VINDO AO CEX
    echo     Cerebro Empresarial X -- o X eh a SUA marca
    echo   ============================================================
    echo.
    echo   Vamos configurar o CEX para a sua empresa.
    echo   Sao ~13 perguntas rapidas ^(5 minutos^).
    echo.
    python _tools/cex_bootstrap.py
    echo.
    echo   Pronto! Para iniciar o CEX: boot\cex.cmd
    echo.
    pause
)

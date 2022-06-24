mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
\n\
\n\
[theme]\n\
base='light'\n\
" > ~/.streamlit/config.toml




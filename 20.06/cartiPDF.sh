#!/bin/bash

# URL-ul paginii IMDb Top 250
url="https://cartigratis.com/categ/top-100"

# Descarcă conținutul paginii utilizând curl
page_content=$(curl -s "$url")
echo $page_content

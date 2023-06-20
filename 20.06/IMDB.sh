#!/bin/bash

# URL-ul paginii IMDb Top 250
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# Descarcă conținutul paginii utilizând curl
page_content=$(curl -s "$url")
echo $page_content
# Extrage titlurile filmelor din conținutul paginii
echo $page_content | egrep -o '(<td class="titleColumn">.{160})' | awk -F '[<>]' '{print $3,$5}'
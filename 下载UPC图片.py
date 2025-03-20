import os
import requests
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import time
import random



# 200个随机user agent 反爬虫
USER_AGENT_LIST = [
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2113.12 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4890.17 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4994.72 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.1638.2 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3056.26 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.1459.70 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4781.46 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4720.11 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4761.51 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1970.12 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3573.3 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4904.55 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3456.57 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3274.83 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.1118.78 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2514.96 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4532.54 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.1545.32 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4124.79 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4864.20 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4178.15 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2298.28 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1167.41 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2897.93 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.2342.79 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.1627.9 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.1197.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4268.100 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4133.94 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.1112.96 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4245.40 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2606.56 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2478.45 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4735.85 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4936.79 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4442.87 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2230.5 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3554.62 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.3305.8 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2633.64 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1570.6 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4342.77 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1494.43 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1425.1 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4541.99 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2013.82 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4739.38 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4934.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4953.12 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3539.17 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2004.37 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1429.42 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3040.49 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2289.86 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.1883.47 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4884.5 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4008.20 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2705.7 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4228.90 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3970.82 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.1164.94 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4492.100 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3951.53 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4181.19 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.1086.69 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.2958.61 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2010.87 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2058.68 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4690.17 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1619.29 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.1280.16 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.1686.24 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1613.76 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3940.31 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4036.21 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3660.6 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2011.80 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4752.1 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.2792.17 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.2114.28 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3513.90 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4874.35 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4331.38 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1886.14 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2879.37 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4668.79 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3538.87 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.3854.60 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2726.67 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4283.95 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2343.80 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.2025.100 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.1128.54 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2591.92 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.3087.31 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2818.35 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.1050.28 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4530.32 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.1116.82 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2747.44 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3018.62 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4544.74 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4003.85 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3463.72 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3501.32 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4381.53 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.2193.22 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3517.68 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.1471.55 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2229.73 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4520.38 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3730.93 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4891.94 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3684.71 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4795.21 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3711.92 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.2934.20 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2794.60 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3312.34 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.2208.16 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4941.37 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4205.43 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4371.75 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3881.59 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3958.13 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.1997.28 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4511.89 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1009.99 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.2215.86 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.1187.81 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.3888.2 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3439.8 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.1515.18 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2334.59 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.1024.97 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1280.71 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3830.92 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2982.85 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1470.13 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4752.98 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4814.18 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1439.89 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3867.26 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2724.44 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3005.34 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3586.64 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1622.76 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.1588.27 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2352.100 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4707.9 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2408.50 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4539.43 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4945.93 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.1911.64 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.2063.78 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4301.38 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.1704.86 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4517.66 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.1616.70 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4134.59 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.1080.43 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.2769.30 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4153.6 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3117.91 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.1947.62 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3491.39 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2282.38 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4392.53 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4482.55 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3552.43 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.1630.74 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.1298.84 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4764.43 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2263.8 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1387.75 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3281.63 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3428.97 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4179.93 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.2576.21 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2384.24 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; x86_64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.3492.37 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.1110.36 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2850.37 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3916.77 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Win64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3354.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Intel Mac; rv:90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4132.53 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1321.10 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:96) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4066.36 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2179.89 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2662.78 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2138.54 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; x86_64; rv:94) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4908.31 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2172.13 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.3254.32 Safari/537.36',
	'Mozilla/5.0 (Linux x86_64; Intel Mac; rv:98) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.1138.98 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:95) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4075.3 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Intel Mac; rv:99) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2242.72 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.3658.97 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; x86_64; rv:93) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3181.96 Safari/537.36',
	'Mozilla/5.0 (Mac OS X 10_15_7; Win64; rv:92) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2780.23 Safari/537.36',
]


def get_user_agent():
	return random.choice(USER_AGENT_LIST)


def check_data(data, code):
	has_numeric_start = False
	has_x_start = False

	for line in data:
		if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
			has_numeric_start = True
		elif line.startswith('X'):
			has_x_start = True

	# 检查条件 1：既有数字开头也有X开头
	if has_numeric_start and has_x_start:
		messagebox.showwarning("警告", "不要乱搞，同一批不能既有数字开头和X开头，请分开处理")
		return False

	# 检查条件 2：只有数字开头，但 code 等于 Code128
	if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')) and code == "Code128":
		messagebox.showwarning("警告", "数字开头必须选择UPC-A.")
		return False

	# 检查条件 3：X 开头，但 code 等于 UPC-A
	if line.startswith('X') and code == "UPCA":  # 假设 "UPCA" 是映射后的值
		messagebox.showwarning("警告", "X开头必须选择Code128.")
		return False

	return True

# 下载图片的函数
def download_images():
    # 获取用户输入的参数
    code_text = code_combobox.get()
    # 根据显示文本获取实际值
    code = display_to_value_map.get(code_text)

    dpi = dpi_entry.get()
    imagetype = imagetype_combobox.get()
    save_dir = save_dir_var.get()
    #data = data_text.get("1.0", tk.END).strip().split("\n")  # 获取多行数据并拆分为列表
    data = [line.strip() for line in data_text.get("1.0", tk.END).splitlines() if line.strip()]

    if not check_data(data, code):
	    return
    # 检查保存目录是否为空
    if not save_dir:
        messagebox.showerror("错误", "请选择保存目录！")
        return

    # 检查数据是否为空
    if not data:
        messagebox.showerror("错误", "请输入至少一个数据！")
        return

    # 禁用下载按钮，防止重复点击
    download_button.config(state=tk.DISABLED)

    # 遍历每个数据并下载图片
    total = len(data)  # 总任务数
    for index, item in enumerate(data, start=1):
        if not item.strip():  # 跳过空行
            continue

        # 更新状态标签
        status_label.config(text=f"正在下载第 {index} 个（共 {total} 个）...")
        root.update()  # 强制刷新界面

        params = {
            "data": item.strip(),
            "code": code,
            "dpi": dpi,
            "imagetype": imagetype,
            "download": "true"
        }
        print(params)

        # 目标 URL
        url = "https://barcode.tec-it.com/barcode.ashx"

        # 发送 GET 请求下载图片，使用随机 User-Agent
        headers = {
            "User-Agent": get_user_agent()
        }

        # 发送 GET 请求下载图片
        response = requests.get(url, params=params, headers=headers)

        # 检查请求是否成功
        if response.status_code == 200:
            # 指定保存目录和文件名
            file_name = f"{item.strip()}.{imagetype.lower()}"  # 文件名
            save_path = os.path.join(save_dir, file_name)  # 完整保存路径

            # 保存图片到指定目录
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"图片已保存到: {save_path}")
        else:
            print(f"请求失败，状态码: {response.status_code}")
        #防止过快请求被屏蔽，暂停1秒休息一会
        time.sleep(1)

    # 下载完成后更新状态标签
    status_label.config(text="全部下载完成！")
    messagebox.showinfo("完成", "图片下载完成！")

    # 重新启用下载按钮
    download_button.config(state=tk.NORMAL)

# 选择保存目录的函数
def select_save_dir():
    directory = filedialog.askdirectory()
    if directory:
        save_dir_var.set(directory)

def center_window(window, width, height):
    # 获取屏幕的宽度和高度
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口应该放置的x和y坐标，使其居中
    position_top = int(screen_height / 2 - height / 2) - 50
    position_right = int(screen_width / 2 - width / 2)

    # 设置窗口的位置和大小
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

# 创建主窗口
root = tk.Tk()
root.title("批量下载UPC条形码————by lixiang")

# 设置窗口大小
#root.geometry("800x600")

# 调用函数将窗口放置在屏幕中央
center_window(root, 800, 600)

# 设置应用程序图标（仅适用于 Windows）
# 图标文件必须为 .ico 格式
root.iconbitmap('imgs/logo.ico')


# 将 RGB(240, 240, 240) 转换为十六进制颜色值
title_bg_color = "#{:02x}{:02x}{:02x}".format(240, 240, 240)

# 添加标题
title_label = tk.Label(
    root,
    text="批量下载UPC条形码",
    font=("Arial", 20, "bold"),  # 设置字体大小和样式
    bg=title_bg_color,  # 背景颜色
    fg="black"  # 字体颜色
)
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # 将标题放置在顶部居中

# 创建一个 Frame 用于放置控件
center_frame = ttk.Frame(root)
center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 创建控件
# 1. Code 下拉选项框
code_label = ttk.Label(center_frame, text="版本:")
code_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
# 显示文本和实际值的映射字典
display_to_value_map = {
    "UPCA (数字开头)": "UPCA",
    "Code128 (X开头)": "Code128"
}
code_combobox = ttk.Combobox(center_frame, values=["UPCA (数字开头)", "Code128 (X开头)"], state="readonly")
code_combobox.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
code_combobox.set("UPCA (数字开头)")  # 默认值

# 2. DPI 输入框
dpi_label = ttk.Label(center_frame, text="图片分辨率 (DPI):")
dpi_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
dpi_entry = ttk.Entry(center_frame)
dpi_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
dpi_entry.insert(0, "300")  # 默认值

# 3. 图片格式下拉选项框
imagetype_label = ttk.Label(center_frame, text="图片格式:")
imagetype_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
imagetype_combobox = ttk.Combobox(center_frame, values=["jpg", "png"], state="readonly")
imagetype_combobox.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
imagetype_combobox.set("jpg")  # 默认值

# 4. Data 文本框
data_label = ttk.Label(center_frame, text="UPC编号 (一行一个):")
data_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.NW)
data_text = tk.Text(center_frame, height=10, width=50)
data_text.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

# 5. 保存目录
save_dir_label = ttk.Label(center_frame, text="保存目录:")
save_dir_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
save_dir_var = tk.StringVar()
save_dir_entry = ttk.Entry(center_frame, textvariable=save_dir_var, width=50)
save_dir_entry.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)
save_dir_button = ttk.Button(center_frame, text="选择目录", command=select_save_dir)
save_dir_button.grid(row=4, column=2, padx=10, pady=10, sticky=tk.W)

# 6. 下载按钮
download_button = ttk.Button(center_frame, text="开始下载", command=download_images)
download_button.grid(row=5, column=1, padx=10, pady=20, sticky=tk.W)

# 7. 状态标签
status_label = ttk.Label(center_frame, text="", font=("Arial", 12))
status_label.grid(row=6, column=0, columnspan=3, pady=10)

# 运行主循环
root.mainloop()


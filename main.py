import urllib.request

url = "https://old.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i=58018684535715055&A=1"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        print("✅ داده دریافت شد:")
        print(data[:1000])  # نمایش ۱۰۰۰ کاراکتر اول
except Exception as e:
    print("⛔ خطا:", e)

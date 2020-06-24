import nltk
from nltk.corpus import stopwords 

article_text="""

هر سرویس کلیه رفتارها و داده های مرتبط با هم را ارسال می کند. اگر ما نیاز به ایجاد یک ویژگی جدید داریم، تمام تغییرات باید فقط در یک سرویس واحد، بومی سازی شوند.
وقتی ما از خدمات میکروسرویس استفاده می کنیم، باید در رعایت هر سه اصل طراحی نظم داشته باشیم. این تنها راه برای دستیابی به پتانسیل کامل معماری خدمات کوچک است. از دست دادن هر یک از آنها، باعث می‌شود تا به سمت یک الگوی نامناسب پیش برویم. بدون یک هدف واحد، هر سرویس هنوز هم می تواند به صورت مجزا کارهای زیادی انجام دهد، اما به عنوان چندین سرویس یکپارچه و در حال رشد کار نمی‌کنند. در این صورت، در حالی که هزینه عملیاتی را به صورت کامل پرداخت می کنیم، مزایای کاملی از معماری میکروسرویس دریافت نخواهیم کرد.
بدون اتصال آزاد، تغییرات در یک سرویس، بر روی سایر خدمات تأثیر می گذارد. بنابراین ما نمی توانیم سریع و با خیال راحت تغییرات را اعمال کنیم. این امر به معنای از دست دادن اصلی ترین مزیت معماری خدمات کوچک است. مهمتر از همه، مسائل ناشی از نداشتن اتصال آزاد می تواند فاجعه بار باشد، که به عنوان مثال ناسازگاری یا حتی از بین رفتن داده ها، از جمله عواقب آن است. بدون انسجام بالا، ما با یک سیستم یکپارچه توزیع شده رو به رو هستیم. مجموعه ای از سرویس های آشفته که باید برای ایجاد یک ویژگی واحد، در همان زمان تغییر کرده و مستقر شوند. یک سیستم یکپارچه توزیع شده، به دلیل پیچیدگی و هزینه هماهنگی خدمات متعدد در بین چندین تیم، بسیار ضعیف تر از یک سیستم یکپارچه متمرکز عمل می‌کند.
خدمات میکروسرویس به معنای سرویسی که تعداد کمی خط کد داشته باشد یا کارهای میکرو ایفا کند، نیست. این تصور غلط ناشی از نام میکروسرویس است. هدف از معماری میکروسرویس این نیست که تا حد امکان خدمات کوچک داشته باشید. خدمات تا زمانی که سه اصل فوق را رعایت کنند، می توانند پیچیده و اساسی باشند.

""" 

sentence_list = nltk.sent_tokenize(article_text)

persian_sw = open('stopwords-fa.txt','r').read()

stop_words= persian_sw.split('\n')

word_frequencies = {}
for word in nltk.word_tokenize(article_text):
    if word not in stop_words:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
            
maximum_frequncy = max(word_frequencies.values())
 
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
                    
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
 
summary = ' '.join(summary_sentences)
print(summary)


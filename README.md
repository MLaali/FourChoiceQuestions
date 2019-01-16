# FourChoiceQuestions
<p dir="rtl">
 این کد  یک فایل PDF  تولید می کند که تعداد چهار دسته سوال تستی پشت سر در آن قرار دارد. در هر دسته از سوال ها گزینه هاو ترتیب سوال ها تصادفی است.
 برای هر دسته سوال یک پاسخ نامه هم طراحی شود و همچنین هر دسته از سوال ها شامل یک بخش مشترک (برای همه دسته ها) تشرحی هم می باشد.
</P><p dir="rtl">
 برای اینکه این کد کار کند ابتدا باید برنامه generate.py اجرا شود تا کلیه سوال ها با گزینه هایش به شکل خام ایجاد شود.
این برنامه با توجه به تعداد سوال هایی که در این فایل مشخص شده  ( عدد ۳۰ که در پایین قرار گرفته) تعدادی سوال خام تولید می کند که باید توسط طراح سوال با کد های لاتک پر شود.
 فایل های تولید این ساختار نام گذاری را دارد:
        انتهای نام فایل هر سوال عدد صفر است و انتهای نام فایل گزینه ها به ترتیب شماره های ۱ تا ۴.
         بنابرین مثلا ques010.tex مربوط به سوال اول و ques013.tex  گزینه سوم سوال اول است.
</P><p dir="rtl">
  در زمان طراحی گزینه های سوال ها، ابتدای هر گزینه که صحیح باشد با قرار دادن دستور correct\ یک علامت تیک در کنار آن گزینه چاپ می شود. از این تیک برای پیدا کردن گزینه صحیح استفاده خواهد می شود
 بعد از طراحی کامل سوال ها چاپ این تیک را می توان با غیر فعال کردن تمام تیک ها (در داخل فایل MyExam.tex محل آن مشخص شده) لغو کرد.
</P><p dir="rtl">
 در صورتی که لازم باشد شکل گزینه ها عوض شود کافی است که در انتهای صورت سوال عبارت
 \renewcommand{\qestionType}{op2}
 چاپ شود
 به عنوان نمونه برنامه  generate.py  در انتهای اولین سوال خام از  دسته اول (در دسته های دیگر در محل تصادفی قرار خواهد گرفت)  این  عبارت را قرار داده است.
</P>
</P><p dir="rtl">
در پایان لازم برنامه MyExam.tex در لاتک  باXeLaTex اجرا شود تا فایل PDF نهایی ایجاد گردد
</P>

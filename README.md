# สิ่งที่ต้องลงก่อนทำโปรเจค

* python -m venv venv
* venv\Scripts\activate 
* pip install -r requirements.txt

# โค้ดสำหรับ Testing 

* py -m unittest -v tests/test_get_answer.py
* py -m nose2 -v --with-coverage
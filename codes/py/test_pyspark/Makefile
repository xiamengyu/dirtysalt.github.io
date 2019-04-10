run:
	rm -rf outputs
	spark-submit --master "spark://mac:7077" --conf "spark.pyspark.appMasterEnv.PYSPARK_PYTHON=venv/bin/python" --py-files venv.zip,app.zip  entry/main.py file:///Users/dirlt/codes/py/test_pyspark/data.json file:///Users/dirlt/codes/py/test_pyspark/outputs

pack:
	echo "make app.zip"; zip -rq app.zip share

pack_venv:
	echo "make venv.zip"; cd venv; zip -rq ../venv.zip *; cd ..

copy:
	rsync -avrz Makefile app.zip venv.zip entry ~/playbook/test_pyspark/

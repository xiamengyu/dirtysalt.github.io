run:
	rm -rf outputs
	spark-submit --master "spark://mac:7077"  --py-files app.zip main.py file://`pwd`/data.json file://`pwd`/outputs/

pack:
	echo "make app.zip"; zip -rq app.zip share

copy:
	mkdir -p temp_build
	rsync -avrz Makefile app.zip entry data.json ./temp_build/

emr_run:
	aws emr add-steps --cluster-id j-2H1HLOUJ20QPY --steps Type=spark,Name=ParquetConversion,Args=[--deploy-mode,cluster,--master,yarn,--conf,spark.yarn.submit.waitAppCompletion=true,--conf,spark.yarn.appMasterEnv.PYSPARK_PYTHON=./venv/bin/python,--conf,spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON=./venv/bin/python,--archives,s3a://s3_bucket/test_pyspark/venv.zip#venv,--py-files,s3a://s3_bucket/test_pyspark/app.zip,s3a://s3_bucket/test_pyspark/main.py],ActionOnFailure=CONTINUE

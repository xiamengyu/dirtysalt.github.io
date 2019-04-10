run:
	rm -rf outputs
	spark-submit --master "spark://mac:7077"  --py-files app.zip entry/main.py file://`pwd`/data.json file://`pwd`/outputs/

pack:
	echo "make app.zip"; zip -rq app.zip share

copy:
	mkdir -p temp_build
	rsync -avrz Makefile app.zip entry data.json ./temp_build/

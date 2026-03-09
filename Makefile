setup:
	pip install -r assets/requirements.txt

pipeline: clean
	python load_data.py
	python src/summary_table.py
	python src/analysis.py
	python src/subsets.py

dashboard:
	streamlit run src/dashboard.py --server.port 8000 --server.address localhost

clean:
	rm -rf cell-count.db assets/boxes.json assets/requested_stats.txt
	rm -rf assets/sample.csv src/__pycache__

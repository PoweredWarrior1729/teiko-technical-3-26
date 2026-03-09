setup:
	pip install -r assets/requirements.txt
	rm cell-count.db assets/boxes.json

pipeline:
	python load_data.py
	python src/summary_table.py
	python src/analysis.py
	python src/subsets.py

dashboard:
	streamlit run src/dashboard.py --server.port 8000 --server.address localhost

clean:
	rm cell-count.db assets/boxes.json
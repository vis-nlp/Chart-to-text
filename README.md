# Chart-to-Text: A Large-Scale Benchmark for Chart Summarization

* Authors: Shankar Kantharaj, Rixie Tiffany Ko Leong, Xiang Lin, [Ahmed Masry](https://sites.google.com/view/ahmedmasry/), Megh Thakkar, Enamul Hoque, Shafiq Joty
* Paper Link: [Chart-to-Text](https://aclanthology.org/2022.findings-acl.177/)

## Chart-to-Text Dataset
Each dataset folder ([Statiata](https://github.com/vis-nlp/Chart-to-text/tree/main/statista_dataset/dataset) or [Pew](https://github.com/vis-nlp/Chart-to-text/tree/main/pew_dataset/dataset)) has the following structure:
```
├── dataset folder                  
│   ├── bboxes # Json files that contain the list of words and their bounidng boxes that were detected in the Chart Images.   
│   │   │   ...
│   │   │   ...
│   └── captions # Text files that contain the target summaries/captions for the chart images.
│   │   │   ...
│   │   │   ...
│   └── data # CSV or Txt files that contain the underlying data table for each chart image.   
│   │   │   ...
│   │   │   ...
│   └── imgs # Chart images (png format)  
│   │   │   ...
│   │   │   ...
│   └── titles # Txt files the contain the titles of the chart images.  
│   │   │   ...
│   │   │   ...
│   └── dataset_splits # CSV files that contain a list of the chart images names for each split (train/val/test)
│   │   │   ...
│   │   │   ...
│   └── **multiColumn** # A folder with the same structure, but it contains the multicolumn charts (e.g., stack bar charts, multi line charts). 
│   │   │   ...
│   │   │   ...
│   └── metadata.csv # A csv file that contain extra metadata that were saved during the crawling process (title, x-axis label, y-axis label, ..etc).
│   └── sta.txt # A text file with some statistics about the data in the folder.  
```

## Models

### BART or T5
Please refer to [Bart-T5](https://github.com/vis-nlp/Chart-to-text/tree/main/baseline_models/bart_t5)

### LogicNLG 
Please refer to [LogicNLG](https://github.com/vis-nlp/Chart-to-text/tree/main/baseline_models/LogicNLG)

### Chart2Text
Please refer to [Chart2Text](https://github.com/vis-nlp/Chart-to-text/tree/main/baseline_models/Chart2Text)

# Evaluation
The metrics used in this work are listed in [evaluation_metrics](https://github.com/vis-nlp/Chart-to-text/tree/main/evaluation_metrics). For each metric, we have steps.txt which presents the steps to setup and run the metric.
# Contact
If you have any questions about this work, please contact **Ahmed Masry** using the following email addresses: **amasry17@ku.edu.tr** or **ahmed.elmasry24653@gmail.com**. 
Please note that my school email which was mentioned in the paper (**masry20@yorku.ca**) has been deactivated since I have already graduated. 

# Reference
Please cite our paper if you use our models or dataset in your research. 

```
@inproceedings{kantharaj-etal-2022-chart,
    title = "Chart-to-Text: A Large-Scale Benchmark for Chart Summarization",
    author = "Kantharaj, Shankar  and
      Leong, Rixie Tiffany  and
      Lin, Xiang  and
      Masry, Ahmed  and
      Thakkar, Megh  and
      Hoque, Enamul  and
      Joty, Shafiq",
    editor = "Muresan, Smaranda  and
      Nakov, Preslav  and
      Villavicencio, Aline",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.277",
    doi = "10.18653/v1/2022.acl-long.277",
    pages = "4005--4023",
}
```

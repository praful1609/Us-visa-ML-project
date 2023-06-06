from collections import namedtuple #tuple is immutable and namedtuple is mutable

DataIngestionConfig: namedtuple("DataIngestionConfig", 
                                ["dataset_download_url",
                                 "raw_data_dir",
                                 "ingested_train_dir",
                                 "ingested_test_dir"])

DataValidationConfig: namedtuple("DataValidationConfig", 
                                 ["scheme_file_dir"])

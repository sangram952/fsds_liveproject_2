#this will be specifically for output files
#any thing that genrates output is called as artifact
#


from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",
["train_file_path","test_file_path","is_ingested","message"])
import os,sys
from src.logger import logging
from src.exception import CustomException
from src.pipeline.training_pipeline import TrainingPipeline
from src.logger import logging
import os ,sys


def main():
    try:
        pipeline = TrainingPipeline()
        pipeline.start_training_pipeline()
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__ == "__main__":
    main()

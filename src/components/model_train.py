import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor   # pyright: ignore[reportMissingImports]
from sklearn.ensemble import (
     AdaBoostRegressor ,
     RandomForestRegressor ,
     GradientBoostingRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor   
from xgboost import XGBRegressor # pyright: ignore[reportMissingImports]
from sklearn.metrics import r2_score

from src.utils import save_object , evaluate_model
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts" , "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_training(self , train_array , test_array ):
          try:
               logging.info("split training and test input data")
               X_train = train_array[:, :-1]
               y_train = train_array[:, -1]
               X_test = test_array[:, :-1]
               y_test = test_array[:, -1]

               models={
                    "random Forest" : RandomForestRegressor(),
                    "Decision Tree" : DecisionTreeRegressor(),
                    "Gradient Boosting" : GradientBoostingRegressor(),
                    "Linear regression": LinearRegression(),
                    "K Nearest Neighbour": KNeighborsRegressor(),
                    "XGBClassifier" : XGBRegressor() ,
                    "CatBoosting Classifier" : CatBoostRegressor(verbose=False),
                    "Adaboosting Classifier" : AdaBoostRegressor()

               }

               model_report:dict=evaluate_model(x_train=X_train , y_train=y_train , x_test=X_test , y_test=y_test ,
                                                models=models)
               
               ## To get Best Model score from dict
               best_model_score = max(sorted(model_report.values()))

               ## to get best model name
               best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

               best_model=models[best_model_name]

               if best_model_score < 0.6 :
                    raise CustomException("No best Model found", sys)
               logging.info(f"Best found model on both training and testing dataset")     

               save_object(
                    file_path=self.model_trainer_config.trained_model_file_path ,
                    obj=best_model
               )

               predicted=best_model.predict(X_test)

               score= r2_score(y_test , predicted) 
               return score

          except Exception as e:
               raise CustomException(e , sys)

        
          
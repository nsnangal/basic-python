import vectorbt as vbt
import pandas as pd
import itertools
import logging
from logging_manager import LoggerManager


class UniversalIndicatorRunner:
   
    @LoggerManager.log_function_call(logging.INFO) 
    def __init__(self):
        
        self.results = {}
        self.keystore=[]   
        self.output_arguments=[] 
        self.loggerobj=LoggerManager()
        self.logger=self.loggerobj.get_logger()
        
    @LoggerManager.log_function_call(logging.INFO)   
    def run_indicators(self, indicators: list):
        """
        Run any indicator with multiple inputs and param sets.
        Each item in `indicators` must be a dict like:
        {
            'name': 'RSI',
            'source': 'talib' or 'custom',
            'input_sets': [ {'real': close1}, {'real': close2}, ... ],
            'param_grid': { 'timeperiod': [14, 21, 28] }
                    
        }
        """
        for ind in indicators:
            name = ind['name'].upper()
            source = ind.get('source', 'talib').lower()
            input_sets = ind.get('input_sets', [])
            param_grid = ind.get('param_grid', {})
            
            try:
                # Load indicator class
                if source.lower() == 'talib':
                    ind_class = vbt.IndicatorFactory.from_talib(name)
                    
                elif source.lower() == 'custom':
                    ind_class = self._load_custom_indicator(name)
                else:
                    print(f"[SKIP] Unknown source '{source}' for {name}")
                    continue

                # Generate all parameter combinations
                param_names = list(param_grid.keys())
                param_values = list(param_grid.values())
                param_combinations = list(itertools.product(*param_values)) or [{}]
                 

                for i_idx, input_set in enumerate(input_sets):
                    for p_idx, param_values_set in enumerate(param_combinations):
                     
                        param_dict = dict(zip(param_names, param_values_set))
                        key = f"{name}_input{i_idx}_params{p_idx}"
                        self.keystore.append(key)    
                        result = ind_class.run(**input_set, **param_dict)
                        
                        self.output_arguments=ind_class.output_names            #output args
                 
                        self.results[key] = {
                            'result': result,
                            'input_index': i_idx,
                            'params': param_dict,
                            'input': input_set,
                            "output_arguments":self.output_arguments
                             }

            except Exception as e:
                 self.logger.error(f"""We are in run_indicator function(IndicatorRunner.py):
                                   [error in indicator]:{name} failed: {e}""")
                 
    def _load_custom_indicator(self, name):
        """
        Define your custom indicators here.
        """
        if name == 'MYCUSTOM':
            @vbt.indicator_factory(input_names=['close'], param_names=['window'], output_names=['ma'])
            def my_ma(close, window):
                return close.rolling(window).mean()
            return my_ma
        raise ValueError(f"Unknown custom indicator: {name}")
   
    @LoggerManager.log_function_call(logging.INFO)
    def get_all_results(self, name_prefix=None):
        """
        Get all stored results, optionally filtered by indicator name.
        """
        if name_prefix:
            return {keys: values for keys, values in self.results.items() 
                    if keys.startswith(name_prefix.upper())}
        return self.results
    
    @LoggerManager.log_function_call(logging.INFO)
    def get_result_by_key(self, keys):
     results={}
     try:
      for index,key in enumerate(keys):
        
        result_dict = self.results.get(key)
        if result_dict is not None:
         indicator_obj = result_dict['result']
         output= {out_args: getattr(indicator_obj,out_args,None) 
                  for out_args in result_dict["output_arguments"]}  
         results[key]=output         
       
      return results
     except Exception as e:
        self.logger.error(f"""Error while running get_results_by_key() function
               in Indicatorrunner.py  :{e}""")
        


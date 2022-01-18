import kfp
from kfp import dsl
from kfp.components import func_to_container_op

@func_to_container_op
def show_csv(csv_file) -> None:
    s = "CSV {csv_file}"
    return s


@dsl.pipeline(name='Pipeline', description='Example Pipeline')
def first_pipeline():

    # Loads the yaml manifest for each component
    preprocess_data = kfp.components.load_component_from_file('preprocess_data/preprocess_data.yaml')


    # Run download_data task
    preprocess_data_task = preprocess_data()

    # Given the outputs from "decision_tree" and "logistic_regression"
    # the component "show_results" is called to print the results.
    #show_csv(load_task.output)



if __name__ == '__main__':
    kfp.compiler.Compiler().compile(first_pipeline, 'Pipeline.yaml')
    # kfp.Client().create_run_from_pipeline_func(basic_pipeline, arguments={})
import kfp
from kfp import dsl
from kfp.components import func_to_container_op

@func_to_container_op
def show_csv(csv_file) -> None:
    print(f"CSV {csv_file}")


@dsl.pipeline(name='Pipeline', description='Example Pipeline')
def first_pipeline():

    # Loads the yaml manifest for each component
    load = kfp.components.load_component_from_file('load_data/load_data.yaml')


    # Run download_data task
    load_task = load()

    # Given the outputs from "decision_tree" and "logistic_regression"
    # the component "show_results" is called to print the results.
    show_csv(load_task.output)



if __name__ == '__main__':
    kfp.compiler.Compiler().compile(first_pipeline, 'Pipeline.yaml')
    # kfp.Client().create_run_from_pipeline_func(basic_pipeline, arguments={})
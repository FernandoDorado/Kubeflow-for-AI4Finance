import kfp
from kfp import dsl
from kfp.components import func_to_container_op

@kfp.dsl.pipeline(name='Hello World', description='First example')

def echo_pipeline(param_1: kfp.dsl.PipelineParam): 
    my_step = simpleStronglyTypedFunction(i= param_1)

kfp.compiler.Compiler().compile(echo_pipeline, 'echo-pipeline.zip')
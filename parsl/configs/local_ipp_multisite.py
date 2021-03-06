"""The following config uses two IPP executors designed for python apps which may
not show any performance improvements on local threads. This also allows you to
send work to two separate remote executors, or to two separate partitions.
"""
from parsl.config import Config
from parsl.providers import LocalProvider
from parsl.executors.ipp import IPyParallelExecutor

config = Config(
    executors=[
        IPyParallelExecutor(
            label='local_ipp_1',
            engine_dir='engines',
            workers_per_node=1,
            provider=LocalProvider(
                nodes_per_block=1,
                walltime="00:15:00",
                init_blocks=4,
            )
        ),
        IPyParallelExecutor(
            label='local_ipp_2',
            engine_dir='engines',
            workers_per_node=1,
            provider=LocalProvider(
                nodes_per_block=1,
                walltime="00:15:00",
                init_blocks=2,
            )
        )

    ],
)

import asyncio
from temporalio import workflow


@workflow.defn
class Child:
    @workflow.run
    async def run(self):
        await asyncio.sleep(5)
        print("Child completed")


@workflow.defn
class Parent:
    @workflow.run
    async def run(self):
        print("Parent start")
        await workflow.start_child_workflow(Child.run, cancellation_type=workflow.ChildWorkflowCancellationType.ABANDON)
        print("Parent completed")

import asyncio
from temporalio.worker import Worker
from temporalio.client import Client
from workflows import Parent, Child


async def main():
    # Uncomment the line below to see logging
    # logging.basicConfig(level=logging.INFO)

    # Start client
    client = await Client.connect("localhost:7233")

    # While the worker is running, use the client to run the workflow and
    # print out its result. Note, in many production setups, the client
    # would be in a completely separate process from the worker.
    await client.start_workflow(
        Parent.run,
        id="hello-activity-workflow-id",
        task_queue="hello-activity-task-queue",
    )
    print("Parent start")
    # Run a worker for the workflow
    w = Worker(
        client,
        task_queue="hello-activity-task-queue",
        workflows=[Parent, Child],
        activities=[],
    )
    await w.run()


if __name__ == "__main__":
    asyncio.run(main())


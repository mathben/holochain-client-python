from holochain_client.api.app.client import AppClient
from holochain_client.api.admin.client import AdminClient

from holochain_client.api.app.client import AppClient

import asyncio
import sys


async def run() -> int:
    client = AppClient("ws://127.0.0.1:8888")

    await client.connect()
    info = await client.app_info("my_happ")

    cell_id = info.cell_id_for_role("main")  # helper à écrire si absent
    result = await client.call_zome(
        cell_id=cell_id,
        zome_name="my_zome",
        fn_name="create_thing",
        payload={"content": "hello"},
    )
    print(result)

    await client.close()


def main() -> int:
    print("Running...")
    return asyncio.run(run())


if __name__ == "__main__":
    sys.exit(main())

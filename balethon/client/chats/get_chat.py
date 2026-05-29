from typing import Union

import balethon
from ...objects import Chat
from ...errors import RPCError
from ...enums import ChatType


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> Chat:
        if isinstance(chat_id, int):
            return await self.auto_execute("post", "getChat", locals())
        if isinstance(chat_id, str):
            chat_id = f"@{chat_id.lstrip('@')}".lower()
            return await self.auto_execute("post", "getChat", locals())

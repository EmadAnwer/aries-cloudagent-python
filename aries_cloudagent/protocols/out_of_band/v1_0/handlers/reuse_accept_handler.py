"""Handshake Reuse Accepted Message Handler under RFC 0434."""

from .....messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)

from ..manager import OutOfBandManager, OutOfBandManagerError
from ..messages.reuse_accept import HandshakeReuseAccept


class HandshakeReuseAcceptMessageHandler(BaseHandler):
    """Handler class for Handshake Reuse Accepted Message Handler under RFC 0434."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Handle Handshake Reuse Accepted Message Handler under RFC 0434.

        Args:
            context: Request context
            responder: Responder callback
        """
        self._logger.debug(f"HandshakeReuseAcceptMessageHandler called with context {context}")
        assert isinstance(context.message, HandshakeReuseAccept)

        session = await context.session()
        mgr = OutOfBandManager(session)
        try:
            await mgr.receive_reuse_accepted_message(
                reuse_accepted_msg=context.message,
                reciept=context.message_receipt,
                conn_record=context.connection_record,
            )
        except OutOfBandManagerError as e:
            self._logger.exception(f"Error processing Handshake Reuse Accept message, {e}")

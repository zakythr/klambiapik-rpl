from __future__ import unicode_literals, absolute_import

import json
import unittest

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    AudioSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.audio_message = AudioSendMessage(
            original_content_url='http://laguaz.net/listen-song/pasar-bisa-diciptakan-vQ9JGckNpS',
            duration=240000
        )

        self.message = [{
            "type": "audio",
            "originalContentUrl": "http://laguaz.net/listen-song/pasar-bisa-diciptakan-vQ9JGckNpS",
            "duration": 240000,
        }]

    @responses.activate
    def test_push_audio_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.audio_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "to",
                "messages": self.message
            }
        )

    @responses.activate
    def test_reply_audio_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.audio_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply')
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                "messages": self.message
            }
        )

    @responses.activate
    def test_multicast_audio_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200
        )

        self.tested.multicast(['to1', 'to2'], self.audio_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ['to1', 'to2'],
                "messages": self.message
            }
        )


if __name__ == '__main__':
    unittest.main()
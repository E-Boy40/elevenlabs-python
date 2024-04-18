# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.do_dubbing_response import DoDubbingResponse
from ..types.dubbing_metadata_response import DubbingMetadataResponse
from ..types.http_validation_error import HttpValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DubbingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def dub_a_video_or_an_audio_file(
        self,
        *,
        mode: typing.Optional[str] = None,
        file: typing.Optional[core.File] = None,
        csv_file: typing.Optional[core.File] = None,
        foreground_audio_file: typing.Optional[core.File] = None,
        background_audio_file: typing.Optional[core.File] = None,
        name: typing.Optional[str] = None,
        source_url: typing.Optional[str] = None,
        source_lang: typing.Optional[str] = None,
        target_lang: str,
        num_speakers: typing.Optional[int] = None,
        watermark: typing.Optional[bool] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        highest_resolution: typing.Optional[bool] = None,
        dubbing_studio: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DoDubbingResponse:
        """
        Dubs provided audio or video file into given language.

        Parameters:
            - mode: typing.Optional[str]. automatic or manual.

            - file: typing.Optional[core.File]. See core.File for more documentation

            - csv_file: typing.Optional[core.File]. See core.File for more documentation

            - foreground_audio_file: typing.Optional[core.File]. See core.File for more documentation

            - background_audio_file: typing.Optional[core.File]. See core.File for more documentation

            - name: typing.Optional[str]. Name of the dubbing project.

            - source_url: typing.Optional[str]. URL of the source video/audio file.

            - source_lang: typing.Optional[str]. Source language.

            - target_lang: str. The Target language to dub the content into. Can be none if dubbing studio editor is enabled and running manual mode

            - num_speakers: typing.Optional[int]. Number of speakers to use for the dubbing.

            - watermark: typing.Optional[bool]. Whether to apply watermark to the output video.

            - start_time: typing.Optional[int]. Start time of the source video/audio file.

            - end_time: typing.Optional[int]. End time of the source video/audio file.

            - highest_resolution: typing.Optional[bool]. Whether to use the highest resolution available.

            - dubbing_studio: typing.Optional[bool]. Whether to prepare dub for edits in dubbing studio.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.dub_a_video_or_an_audio_file(
            target_lang="target_lang",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/dubbing"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "mode": mode,
                        "name": name,
                        "source_url": source_url,
                        "source_lang": source_lang,
                        "target_lang": target_lang,
                        "num_speakers": num_speakers,
                        "watermark": watermark,
                        "start_time": start_time,
                        "end_time": end_time,
                        "highest_resolution": highest_resolution,
                        "dubbing_studio": dubbing_studio,
                    }
                )
            )
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "mode": mode,
                            "name": name,
                            "source_url": source_url,
                            "source_lang": source_lang,
                            "target_lang": target_lang,
                            "num_speakers": num_speakers,
                            "watermark": watermark,
                            "start_time": start_time,
                            "end_time": end_time,
                            "highest_resolution": highest_resolution,
                            "dubbing_studio": dubbing_studio,
                        }
                    )
                ),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(
                remove_none_from_dict(
                    {
                        "file": file,
                        "csv_file": csv_file,
                        "foreground_audio_file": foreground_audio_file,
                        "background_audio_file": background_audio_file,
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(DoDubbingResponse, construct_type(type_=DoDubbingResponse, object_=_response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_dubbing_project_metadata(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DubbingMetadataResponse:
        """
        Returns metadata about a dubbing project, including whether it's still in progress or not

        Parameters:
            - dubbing_id: str. ID of the dubbing project.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.get_dubbing_project_metadata(
            dubbing_id="dubbing_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/dubbing/{jsonable_encoder(dubbing_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(DubbingMetadataResponse, construct_type(type_=DubbingMetadataResponse, object_=_response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_dubbing_project(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Deletes a dubbing project.

        Parameters:
            - dubbing_id: str. ID of the dubbing project.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.delete_dubbing_project(
            dubbing_id="dubbing_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/dubbing/{jsonable_encoder(dubbing_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(typing.Any, construct_type(type_=typing.Any, object_=_response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_dubbed_file(
        self, dubbing_id: str, language_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns dubbed file as a streamed file. Videos will be returned in MP4 format and audio only dubs will be returned in MP3.

        Parameters:
            - dubbing_id: str. ID of the dubbing project.

            - language_code: str. ID of the language.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.get_dubbed_file(
            dubbing_id="dubbing_id",
            language_code="language_code",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/dubbing/{jsonable_encoder(dubbing_id)}/audio/{jsonable_encoder(language_code)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDubbingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def dub_a_video_or_an_audio_file(
        self,
        *,
        mode: typing.Optional[str] = None,
        file: typing.Optional[core.File] = None,
        csv_file: typing.Optional[core.File] = None,
        foreground_audio_file: typing.Optional[core.File] = None,
        background_audio_file: typing.Optional[core.File] = None,
        name: typing.Optional[str] = None,
        source_url: typing.Optional[str] = None,
        source_lang: typing.Optional[str] = None,
        target_lang: str,
        num_speakers: typing.Optional[int] = None,
        watermark: typing.Optional[bool] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        highest_resolution: typing.Optional[bool] = None,
        dubbing_studio: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DoDubbingResponse:
        """
        Dubs provided audio or video file into given language.

        Parameters:
            - mode: typing.Optional[str]. automatic or manual.

            - file: typing.Optional[core.File]. See core.File for more documentation

            - csv_file: typing.Optional[core.File]. See core.File for more documentation

            - foreground_audio_file: typing.Optional[core.File]. See core.File for more documentation

            - background_audio_file: typing.Optional[core.File]. See core.File for more documentation

            - name: typing.Optional[str]. Name of the dubbing project.

            - source_url: typing.Optional[str]. URL of the source video/audio file.

            - source_lang: typing.Optional[str]. Source language.

            - target_lang: str. The Target language to dub the content into. Can be none if dubbing studio editor is enabled and running manual mode

            - num_speakers: typing.Optional[int]. Number of speakers to use for the dubbing.

            - watermark: typing.Optional[bool]. Whether to apply watermark to the output video.

            - start_time: typing.Optional[int]. Start time of the source video/audio file.

            - end_time: typing.Optional[int]. End time of the source video/audio file.

            - highest_resolution: typing.Optional[bool]. Whether to use the highest resolution available.

            - dubbing_studio: typing.Optional[bool]. Whether to prepare dub for edits in dubbing studio.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.dubbing.dub_a_video_or_an_audio_file(
            target_lang="target_lang",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/dubbing"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "mode": mode,
                        "name": name,
                        "source_url": source_url,
                        "source_lang": source_lang,
                        "target_lang": target_lang,
                        "num_speakers": num_speakers,
                        "watermark": watermark,
                        "start_time": start_time,
                        "end_time": end_time,
                        "highest_resolution": highest_resolution,
                        "dubbing_studio": dubbing_studio,
                    }
                )
            )
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "mode": mode,
                            "name": name,
                            "source_url": source_url,
                            "source_lang": source_lang,
                            "target_lang": target_lang,
                            "num_speakers": num_speakers,
                            "watermark": watermark,
                            "start_time": start_time,
                            "end_time": end_time,
                            "highest_resolution": highest_resolution,
                            "dubbing_studio": dubbing_studio,
                        }
                    )
                ),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(
                remove_none_from_dict(
                    {
                        "file": file,
                        "csv_file": csv_file,
                        "foreground_audio_file": foreground_audio_file,
                        "background_audio_file": background_audio_file,
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(DoDubbingResponse, construct_type(type_=DoDubbingResponse, object_=_response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_dubbing_project_metadata(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DubbingMetadataResponse:
        """
        Returns metadata about a dubbing project, including whether it's still in progress or not

        Parameters:
            - dubbing_id: str. ID of the dubbing project.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.dubbing.get_dubbing_project_metadata(
            dubbing_id="dubbing_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/dubbing/{jsonable_encoder(dubbing_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(DubbingMetadataResponse, construct_type(type_=DubbingMetadataResponse, object_=_response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_dubbing_project(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Deletes a dubbing project.

        Parameters:
            - dubbing_id: str. ID of the dubbing project.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.dubbing.delete_dubbing_project(
            dubbing_id="dubbing_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/dubbing/{jsonable_encoder(dubbing_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(typing.Any, construct_type(type_=typing.Any, object_=_response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_dubbed_file(
        self, dubbing_id: str, language_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns dubbed file as a streamed file. Videos will be returned in MP4 format and audio only dubs will be returned in MP3.

        Parameters:
            - dubbing_id: str. ID of the dubbing project.

            - language_code: str. ID of the language.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.dubbing.get_dubbed_file(
            dubbing_id="dubbing_id",
            language_code="language_code",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/dubbing/{jsonable_encoder(dubbing_id)}/audio/{jsonable_encoder(language_code)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci.encryption.internal.streaming import StreamEncryptor, StreamDecryptor
from oci.encryption.internal.utils import convert_to_bytes
from oci.encryption.models import CryptoResult
import io

from oci.encryption.internal.defaults import DEFAULT_MAX_ENCRYPTION_SIZE_SENTINEL


def encrypt(
    **kwargs
):
    """
    Returns data encrypted under the provided master key.

    The master key is used to generate a data encryption key which
    is used directly to encrypt the data.

    The bytes returned in the CryptoResult include a header containing various
    metadata that allows it to be decrypted by the OCI Python SDK and other OCI
    SDKs that support client side encryption.

    Note this data cannot be decrypted using the KMS 'decrypt' APIs.

    :param oci.encryption.MasterKeyProvider master_key_provider: (required)
        A MasterKeyProvider to use for encrypting the data

    :param bytes data: (required)
        The data to be encyrpted. If a string is passed, it will be converted to
        bytes using UTF-8 encoding.  Note that this conversion will require creating
        a copy of the data which may be undesirable for large payloads.

    :param dict encryption_context: (optional)
        The encryption context to use while encrypting the data. This must be a dict where
        all keys and values are strings, and no keys begin with the prefix "oci-".

        This context is used as additional authenticated data for authenticated encryption
        algorithms which support it. The same encryption context must be used upon decryption
        otherwise the call to decrypt will fail. The encryption context is included in the
        header of the encrypted payload, so you do not need to supply it separately upon
        decryption.

    :rtype: oci.encryption.CryptoResult
    """
    _ensure_required_kwargs_present(required_kwargs=['master_key_provider', 'data'], provided_kwargs=kwargs)

    encryption_context = kwargs.get('encryption_context', None)
    # leaves input alone if it is alread bytes, otherwise converts to bytes using default encoding
    # this is for convenience of the caller, but will create a copy of the data if it is not already a
    # bytes-like object
    data = convert_to_bytes(kwargs.get('data'))
    # as long as we only read from the stream, BytesIO does not create a copy of the data so this doesn't
    # add memory overhead
    with io.BytesIO(data) as stream_to_encrypt:
        encryptor = StreamEncryptor(
            master_key_provider=kwargs.get('master_key_provider'),
            stream_to_encrypt=stream_to_encrypt,
            max_encryption_size=None,
            encryption_context=encryption_context,
        )
        return CryptoResult(data=encryptor.read(), encryption_context=encryption_context)


def decrypt(**kwargs):
    """
    Returns a CryptoResult containing decrypted bytes.

    This function requires that 'data' is in the format generated by the
    encrypt functionality in this SDK as well as other OCI SDKs that support
    client side encryption.

    Note this function cannot decrypt data encrypted by the KMS 'encrypt' APIs.

    :param oci.encryption.MasterKeyProvider master_key_provider: (required)
        A MasterKeyProvider to use for decrypting the data.

    :param bytes data: (required)
        The data to be decrypted. If a string is passed, it will be converted to
        bytes using UTF-8 encoding.  Note that this conversion will require creating
        a copy of the data which may be undesirable for large payloads.

    :rtype: oci.encryption.CryptoResult
    """
    _ensure_required_kwargs_present(required_kwargs=['master_key_provider', 'data'], provided_kwargs=kwargs)

    # leaves input alone if it is alread bytes, otherwise converts to bytes using default encoding
    # this is for convenience of the caller, but will create a copy of the data if it is not already a
    # bytes-like object
    data = convert_to_bytes(kwargs.get('data'))
    # as long as we only read from the stream, BytesIO does not create a copy of the data so this doesn't
    # add memory overhead
    with io.BytesIO(data) as stream_to_decrypt:
        decryptor = StreamDecryptor(
            stream_to_decrypt=stream_to_decrypt, master_key_provider=kwargs.get('master_key_provider')
        )
        return CryptoResult(data=decryptor.read(), encryption_context=decryptor.get_encryption_context())


def create_encryption_stream(
    **kwargs
):
    """
    Returns a CryptoResultStream which produces encrypted data based on the underlying stream
    supplied as 'stream_to_encrypt'.

    The master key provider is used to generate a data encryption key which
    is used directly to encrypt the data.

    The returned stream includes a header containing various metadata that
    allows it to be decrypted by the OCI Python SDK and other OCI SDKs that
    support client side encryption.

    Note data encrypted by this CryptoResultStream cannot be decrypted using the KMS 'decrypt' APIs.

    :param oci.encryption.MasterKeyProvider master_key_provider: (required)
        A MasterKeyProvider to use for encrypting the data.

    :param stream stream_to_encrypt: (required)
        The stream to be encrypted.

    :param dict encryption_context: (optional)
        The encryption context to use while encrypting the data. This must be a dict where
        all keys and values are strings, and no keys begin with the prefix "oci-".
        This context is used as additional authenticated data for authenticated encryption
        algorithms which support it. The same encryption context must be used upon decryption
        otherwise the call to decrypt will fail. The encryption context is included in the
        header of the encrypted payload, so you do not need to supply it separately upon
        decryption.

    :param int max_encryption_size: (optional)
        Max number of bytes able to be encrypted by this CryptoResultStream. The default value differs
        based on the algorithm used. For GCM (the default algorithm) the default value is 2147483647 bytes.
        This is provided mainly for use with authenticated encryption algorithms that require verification
        of an authentication tag upon decryption. Because decrypting using these algorithms will buffer
        the entire payload into memory before returning it, this max_encryption_size provides a sanity
        check against encrypting payloads too large to decrypt. This is possible because encryption does not
        require holding the entire payload in memory.

        The 2147483647 byte limit was chosen because that is the maximum number of bytes that can be encrypted or
        decrypted by the OCI Java SDK. This is to avoid users accidentally encrypting payloads in Python that
        cannot be decrypted in Java.

        Explicitly passing this value as None will disable the size check and allow encrypting payloads up to
        the maximum size supported by the algorithm.

    :rtype: oci.encryption.models.CryptoResultStream
    """
    _ensure_required_kwargs_present(required_kwargs=['master_key_provider', 'stream_to_encrypt'], provided_kwargs=kwargs)

    encryption_context = kwargs.get('encryption_context', None)
    max_encryption_size = kwargs.get('max_encryption_size', DEFAULT_MAX_ENCRYPTION_SIZE_SENTINEL)

    return StreamEncryptor(
        master_key_provider=kwargs.get('master_key_provider'),
        stream_to_encrypt=kwargs.get('stream_to_encrypt'),
        max_encryption_size=max_encryption_size,
        encryption_context=encryption_context,
    )


def create_decryption_stream(**kwargs):
    """
    Returns a CryptoResultStream which produces decrypted data based on the underlying stream
    supplied as 'stream_to_decrypt'.

    Note this function cannot decrypt data encrypted by the KMS 'decrypt' APIs.

    :param oci.encryption.MasterKeyProvider master_key_provider: (required)
        A MasterKeyProvider to use for decrypting the data.

    :param stream stream_to_decrypt: (required)
        The stream to be decrypted.

    :rtype: oci.encryption.models.CryptoResultStream
    """
    _ensure_required_kwargs_present(required_kwargs=['master_key_provider', 'stream_to_decrypt'], provided_kwargs=kwargs)

    return StreamDecryptor(
        stream_to_decrypt=kwargs.get('stream_to_decrypt'), master_key_provider=kwargs.get('master_key_provider')
    )


def _ensure_required_kwargs_present(required_kwargs, provided_kwargs):
    missing_required_kwargs = [required_kwarg for required_kwarg in required_kwargs if required_kwarg not in provided_kwargs]
    if missing_required_kwargs:
        raise TypeError('missing keyword argument(s): {}'.format(', '.join(missing_required_kwargs)))

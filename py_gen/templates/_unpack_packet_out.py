:: # Copyright 2013, Big Switch Networks, Inc.
:: #
:: # LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
:: # the following special exception:
:: #
:: # LOXI Exception
:: #
:: # As a special exception to the terms of the EPL, you may distribute libraries
:: # generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
:: # that copyright and licensing notices generated by LoxiGen are not altered or removed
:: # from the LoxiGen Libraries and the notice provided below is (i) included in
:: # the LoxiGen Libraries, if distributed in source code form and (ii) included in any
:: # documentation for the LoxiGen Libraries, if distributed in binary form.
:: #
:: # Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
:: #
:: # You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
:: # a copy of the EPL at:
:: #
:: # http://www.eclipse.org/legal/epl-v10.html
:: #
:: # Unless required by applicable law or agreed to in writing, software
:: # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
:: # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
:: # EPL for the specific language governing permissions and limitations
:: # under the EPL.
::
        version = struct.unpack_from('!B', buf, 0)[0]
        assert(version == const.OFP_VERSION)
        type = struct.unpack_from('!B', buf, 1)[0]
        assert(type == const.OFPT_PACKET_OUT)
        _length = struct.unpack_from('!H', buf, 2)[0]
        assert(_length == len(buf))
        if _length < 16: raise loxi.ProtocolError("packet_out length is %d, should be at least 16" % _length)
        obj.xid = struct.unpack_from('!L', buf, 4)[0]
        obj.buffer_id = struct.unpack_from('!L', buf, 8)[0]
        obj.in_port = struct.unpack_from('!H', buf, 12)[0]
        actions_len = struct.unpack_from('!H', buf, 14)[0]
        obj.actions = action.unpack_list(buffer(buf, 16, actions_len))
        obj.data = str(buffer(buf, 16+actions_len))

#!/usr/bin/env python
# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.
import unittest

try:
    import loxi.of13 as ofp
except ImportError:
    exit("loxi package not found. Try setting PYTHONPATH.")

class TestImports(unittest.TestCase):
    def test_toplevel(self):
        import loxi
        self.assertTrue(hasattr(loxi, "ProtocolError"))
        ofp = loxi.protocol(4)
        self.assertEquals(ofp.OFP_VERSION, 4)
        self.assertTrue(hasattr(ofp, "action"))
        self.assertTrue(hasattr(ofp, "common"))
        self.assertTrue(hasattr(ofp, "const"))
        self.assertTrue(hasattr(ofp, "message"))

    def test_version(self):
        import loxi
        self.assertTrue(hasattr(loxi.of13, "ProtocolError"))
        self.assertTrue(hasattr(loxi.of13, "OFP_VERSION"))
        self.assertEquals(loxi.of13.OFP_VERSION, 4)
        self.assertTrue(hasattr(loxi.of13, "action"))
        self.assertTrue(hasattr(loxi.of13, "common"))
        self.assertTrue(hasattr(loxi.of13, "const"))
        self.assertTrue(hasattr(loxi.of13, "message"))

class TestCommon(unittest.TestCase):
    sample_hello_elem_buf = ''.join([
        '\x00\x01', # type
        '\x00\x0c', # length
        '\x01\x23\x45\x67', # bitmaps[0]
        '\x89\xab\xcd\xef', # bitmaps[1]
    ])

    def test_hello_elem_versionbitmap_pack(self):
        obj = ofp.hello_elem_versionbitmap(bitmaps=[ofp.uint32(0x01234567),ofp.uint32(0x89abcdef)])
        self.assertEquals(self.sample_hello_elem_buf, obj.pack())

    def test_hello_elem_versionbitmap_unpack(self):
        obj = ofp.hello_elem_versionbitmap.unpack(self.sample_hello_elem_buf)
        self.assertEquals(len(obj.bitmaps), 2)
        self.assertEquals(obj.bitmaps[0], ofp.uint32(0x01234567))
        self.assertEquals(obj.bitmaps[1], ofp.uint32(0x89abcdef))

    def test_list_hello_elem_unpack(self):
        buf = ''.join([
            '\x00\x01\x00\x04', # versionbitmap
            '\x00\x00\x00\x04', # unknown type
            '\x00\x01\x00\x04', # versionbitmap
        ])
        l = ofp.unpack_list_hello_elem(buf)
        self.assertEquals(len(l), 2)
        self.assertTrue(isinstance(l[0], ofp.hello_elem_versionbitmap))
        self.assertTrue(isinstance(l[1], ofp.hello_elem_versionbitmap))

class TestOXM(unittest.TestCase):
    def test_oxm_in_phy_port_pack(self):
        import loxi.of13 as ofp
        obj = ofp.oxm.in_phy_port(value=42)
        expected = ''.join([
            '\x80\x00', # class
            '\x02', # type/masked
            '\x08', # length
            '\x00\x00\x00\x2a' # value
        ])
        self.assertEquals(expected, obj.pack())

    def test_oxm_in_phy_port_masked_pack(self):
        import loxi.of13 as ofp
        obj = ofp.oxm.in_phy_port_masked(value=42, value_mask=0xaabbccdd)
        expected = ''.join([
            '\x80\x00', # class
            '\x03', # type/masked
            '\x0c', # length
            '\x00\x00\x00\x2a', # value
            '\xaa\xbb\xcc\xdd' # mask
        ])
        self.assertEquals(expected, obj.pack())

    def test_oxm_ipv6_dst_pack(self):
        import loxi.of13 as ofp
        obj = ofp.oxm.ipv6_dst(value='\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0d\x0f')
        expected = ''.join([
            '\x80\x00', # class
            '\x36', # type/masked
            '\x14', # length
            '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0d\x0f', # value
        ])
        self.assertEquals(expected, obj.pack())

class TestAllOF13(unittest.TestCase):
    """
    Round-trips every class through serialization/deserialization.
    Not a replacement for handcoded tests because it only uses the
    default member values.
    """

    def setUp(self):
        mods = [ofp.action,ofp.message,ofp.common,ofp.oxm]
        self.klasses = [klass for mod in mods
                              for klass in mod.__dict__.values()
                              if hasattr(klass, 'show')]
        self.klasses.sort(key=lambda x: str(x))

    def test_serialization(self):
        expected_failures = [
            ofp.common.action_id,
            ofp.common.action_id_bsn_mirror,
            ofp.common.action_id_bsn_set_tunnel_dst,
            ofp.common.action_id_copy_ttl_in,
            ofp.common.action_id_copy_ttl_out,
            ofp.common.action_id_dec_mpls_ttl,
            ofp.common.action_id_dec_nw_ttl,
            ofp.common.action_id_experimenter,
            ofp.common.action_id_group,
            ofp.common.action_id_header,
            ofp.common.action_id_nicira_dec_ttl,
            ofp.common.action_id_output,
            ofp.common.action_id_pop_mpls,
            ofp.common.action_id_pop_pbb,
            ofp.common.action_id_pop_vlan,
            ofp.common.action_id_push_mpls,
            ofp.common.action_id_push_pbb,
            ofp.common.action_id_push_vlan,
            ofp.common.action_id_set_field,
            ofp.common.action_id_set_mpls_ttl,
            ofp.common.action_id_set_nw_ttl,
            ofp.common.action_id_set_queue,
            ofp.common.flow_stats_entry,
            ofp.common.group_desc_stats_entry,
            ofp.common.instruction,
            ofp.common.instruction_apply_actions,
            ofp.common.instruction_clear_actions,
            ofp.common.instruction_experimenter,
            ofp.common.instruction_goto_table,
            ofp.common.instruction_header,
            ofp.common.instruction_meter,
            ofp.common.instruction_write_actions,
            ofp.common.instruction_write_metadata,
            ofp.common.match_v3,
            ofp.common.meter_band,
            ofp.common.meter_band_drop,
            ofp.common.meter_band_dscp_remark,
            ofp.common.meter_band_experimenter,
            ofp.common.meter_band_header,
            ofp.common.table_feature_prop,
            ofp.common.table_feature_prop_apply_actions,
            ofp.common.table_feature_prop_apply_actions_miss,
            ofp.common.table_feature_prop_apply_setfield,
            ofp.common.table_feature_prop_apply_setfield_miss,
            ofp.common.table_feature_prop_experimenter,
            ofp.common.table_feature_prop_header,
            ofp.common.table_feature_prop_instructions,
            ofp.common.table_feature_prop_instructions_miss,
            ofp.common.table_feature_prop_match,
            ofp.common.table_feature_prop_next_tables,
            ofp.common.table_feature_prop_next_tables_miss,
            ofp.common.table_feature_prop_wildcards,
            ofp.common.table_feature_prop_write_actions,
            ofp.common.table_feature_prop_write_actions_miss,
            ofp.common.table_feature_prop_write_setfield,
            ofp.common.table_feature_prop_write_setfield_miss,
            ofp.message.aggregate_stats_request,
            ofp.message.flow_add,
            ofp.message.flow_delete,
            ofp.message.flow_delete_strict,
            ofp.message.flow_modify,
            ofp.message.flow_modify_strict,
            ofp.message.flow_removed,
            ofp.message.flow_stats_request,
            ofp.message.group_desc_stats_reply,
            ofp.message.group_mod,
            ofp.message.group_stats_reply,
            ofp.message.meter_features_stats_reply,
            ofp.message.meter_stats_reply,
            ofp.message.packet_in,
            ofp.message.table_features_stats_reply,
            ofp.message.table_features_stats_request,
        ]
        for klass in self.klasses:
            def fn():
                obj = klass()
                if hasattr(obj, "xid"): obj.xid = 42
                buf = obj.pack()
                obj2 = klass.unpack(buf)
                self.assertEquals(obj, obj2)
            if klass in expected_failures:
                self.assertRaises(Exception, fn)
            else:
                fn()

    def test_show(self):
        expected_failures = [
            ofp.common.action_id,
            ofp.common.action_id_bsn_mirror,
            ofp.common.action_id_bsn_set_tunnel_dst,
            ofp.common.action_id_copy_ttl_in,
            ofp.common.action_id_copy_ttl_out,
            ofp.common.action_id_dec_mpls_ttl,
            ofp.common.action_id_dec_nw_ttl,
            ofp.common.action_id_experimenter,
            ofp.common.action_id_group,
            ofp.common.action_id_header,
            ofp.common.action_id_nicira_dec_ttl,
            ofp.common.action_id_output,
            ofp.common.action_id_pop_mpls,
            ofp.common.action_id_pop_pbb,
            ofp.common.action_id_pop_vlan,
            ofp.common.action_id_push_mpls,
            ofp.common.action_id_push_pbb,
            ofp.common.action_id_push_vlan,
            ofp.common.action_id_set_field,
            ofp.common.action_id_set_mpls_ttl,
            ofp.common.action_id_set_nw_ttl,
            ofp.common.action_id_set_queue,
            ofp.common.flow_stats_entry,
            ofp.common.group_desc_stats_entry,
            ofp.common.instruction,
            ofp.common.instruction_apply_actions,
            ofp.common.instruction_clear_actions,
            ofp.common.instruction_experimenter,
            ofp.common.instruction_goto_table,
            ofp.common.instruction_header,
            ofp.common.instruction_meter,
            ofp.common.instruction_write_actions,
            ofp.common.instruction_write_metadata,
            ofp.common.match_v3,
            ofp.common.meter_band,
            ofp.common.meter_band_drop,
            ofp.common.meter_band_dscp_remark,
            ofp.common.meter_band_experimenter,
            ofp.common.meter_band_header,
            ofp.common.table_feature_prop,
            ofp.common.table_feature_prop_apply_actions,
            ofp.common.table_feature_prop_apply_actions_miss,
            ofp.common.table_feature_prop_apply_setfield,
            ofp.common.table_feature_prop_apply_setfield_miss,
            ofp.common.table_feature_prop_experimenter,
            ofp.common.table_feature_prop_header,
            ofp.common.table_feature_prop_instructions,
            ofp.common.table_feature_prop_instructions_miss,
            ofp.common.table_feature_prop_match,
            ofp.common.table_feature_prop_next_tables,
            ofp.common.table_feature_prop_next_tables_miss,
            ofp.common.table_feature_prop_wildcards,
            ofp.common.table_feature_prop_write_actions,
            ofp.common.table_feature_prop_write_actions_miss,
            ofp.common.table_feature_prop_write_setfield,
            ofp.common.table_feature_prop_write_setfield_miss,
            ofp.message.aggregate_stats_request,
            ofp.message.flow_add,
            ofp.message.flow_delete,
            ofp.message.flow_delete_strict,
            ofp.message.flow_modify,
            ofp.message.flow_modify_strict,
            ofp.message.flow_removed,
            ofp.message.flow_stats_request,
            ofp.message.packet_in,
        ]
        for klass in self.klasses:
            def fn():
                obj = klass()
                if hasattr(obj, "xid"): obj.xid = 42
                obj.show()
            if klass in expected_failures:
                self.assertRaises(Exception, fn)
            else:
                fn()

if __name__ == '__main__':
    unittest.main()

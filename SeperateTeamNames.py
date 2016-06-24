# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:49:16 2016

@author: James
"""
import win32com.client


def ado():
    '''
    connect with com dispatch objs
    '''
    db = 'PlayersInstance'
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = ('PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = ' + db +  ';')
    conn.Open(DSN)

    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    strsql = "select * from nba"
    rs.Open(strsql, conn, 1, 3)
    t = rs.GetRows()
    conn.Close()
    return t
x = ado()
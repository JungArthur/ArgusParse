import ArgsParse

if __name__ == '__main__':

    find_index = 0

    # convert_string = 'rlacl CONVERT(CHAR(5), dbo.CIM_F_UTC_To_Local(@CreatedTo), 24) + ' ' + CONVERT( CHAR(5), dbo.CIM_F_UTC_To_Local(@CreateTo), 24 )'
    convert_string = 'rlCONVERT(CHAR(5), dbo.CIM_F_UTC_To_Local(@CreateTo)) + ' ' + CONVERT( CHAR(5), dbo.CIM_F_UTC_To_Local(@CreateTo), 24 )'

    ArgsParse.conver_args(convert_string)



dataset_1 {
    int16 field0_length = length(field0)
    int32 field0 = incremental_range(0,100,1)
    string field1 = value("abcd")
}
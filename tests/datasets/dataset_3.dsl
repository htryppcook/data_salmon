dataset {
    int32 field0 = incremental_range(0,100,1)
    string field1 = value("abcd")
    int32 field2 = value(42)
    int32 field3 = ordered_choice(4,8,15,16,23,42)
    ipv4 field4 = random_range("1.2.3.4", "2.3.4.5")
}

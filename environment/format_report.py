def format_report(df1):
    for i, row in df1.iterrows():
        print(i, row.col1, row.col2)
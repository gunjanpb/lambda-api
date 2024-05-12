from lambda_function import list_s3_bucket_contents

def test_list_s3_bucket_contents():
    bucket_name = 'gunjantest'
    assert set(list_s3_bucket_contents(bucket_name)) == set(['dir1', 'dir2'])
    assert set(list_s3_bucket_contents(bucket_name, 'dir2')) == set(['file1', 'file2'])
    assert list_s3_bucket_contents(bucket_name, 'dir1') == []
    assert list_s3_bucket_contents(bucket_name, 'non-existant') == None

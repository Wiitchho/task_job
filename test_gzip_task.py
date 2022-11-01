import os

from gzip_task import main


def test_compression_works(tmp_path):
    d = tmp_path / "logs"
    d.mkdir()
    p = d / "hello.log"
    p.write_text("1" * 10000)

    main(str(d))

    files = os.listdir(str(d))
    assert files == ["hello.log.gz"]

# TODO: make sure the file is actually compressed (i.e. has smaller size than before)

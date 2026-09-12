#target
TARGET = browser.py
#test
TEST_TARGET = test_browser.py
#run
run: $(TARGET)
	python3 $(TARGET) https://example.com/test
#run test
test: $(TEST_TARGET)
	python3 $(TEST_TARGET)

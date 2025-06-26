import py5

def setup():
    py5.size(400, 400)
    py5.background(255)
    py5.fill(0)
    py5.text_size(32)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text("Hello, Py5!", 200, 200)

py5.run_sketch()

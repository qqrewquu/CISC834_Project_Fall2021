#!/usr/bin/env python
from sys import argv

if len(argv) != 2:
    print('usage: %s filename.kv' % argv[0])
    exit(1)


from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock, mainthread
from kivy.uix.label import Label

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import dirname, basename, join

PATH = dirname(argv[1])
TARGET = basename(argv[1])


class KvHandler(FileSystemEventHandler):
    def __init__(self, callback, target, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.callback = callback
        self.target = target

    def on_any_event(self, event):
        if basename(event.src_path) == self.target:
            self.callback()


class KvViewerApp(App):
    def build(self):
        o = Observer()
        o.schedule(KvHandler(self.update, TARGET), PATH)
        o.start()
        Clock.schedule_once(self.update, 1)
        return super(KvViewerApp, self).build()

    @mainthread
    def update(self, *args):
        Builder.unload_file(join(PATH, TARGET))
        Window.remove_widget(Window.children[0])
        try:
            Window.add_widget(Builder.load_file(join(PATH, TARGET)))
        except Exception as e:
            Window.add_widget(Label(text=e.message if e.message else str(e)))


if __name__ == '__main__':
    KvViewerApp().run()
import urwid

def menu(title, choices):
    body = []
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'OK')
    urwid.connect_signal(done, 'click', exit_program)
    
    pile = urwid.Pile([
        response,
        urwid.AttrMap(done, None, focus_map='reversed')
    ])
    filler = urwid.Filler(pile)
    main.original_widget = filler  # <--- artık HATA VERMEZ

def exit_program(button):
    raise urwid.ExitMainLoop()

if __name__ == '__main__':
    choices = ['Ali', 'Ayşe', 'Mehmet', 'Elif', 'Can']
    
    # ✅ WidgetPlaceholder olarak tanımlıyoruz
    main = urwid.WidgetPlaceholder(
        urwid.Padding(menu(u'Seçiniz:', choices), left=2, right=2)
    )

    top = urwid.Overlay(
        main,
        urwid.SolidFill(u'\N{MEDIUM SHADE}'),
        align='center', width=('relative', 60),
        valign='middle', height=('relative', 60),
        min_width=20, min_height=9
    )
    urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

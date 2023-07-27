function main(splash, args)
    splash.private_mode_enabled = false
    local url = args.url
    assert(splash:go(url))
    assert(splash:wait(1))

    local run_tab = assert(splash:select_all(".filterPanelItem___2z5Gb "))
    run_tab[4]:mouse_click()
    assert(splash:wait(1))
    
    splash:set_viewport_full()
    return {
        image = splash:png(),
        html = splash:html(),
    }
end
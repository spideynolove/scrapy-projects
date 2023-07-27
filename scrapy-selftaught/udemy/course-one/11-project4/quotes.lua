function main(splash, args)
    splash.private_mode_enabled = false
    local url = args.url
    assert(splash:go(url))
    assert(splash:wait(3))
    splash:set_viewport_full()
    return {
        image = splash:png(),
        html = splash:html(),
    }
end

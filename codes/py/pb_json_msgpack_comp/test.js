function json_bench(n) {
    keys = []
    pids = []
    for (var i = 0; i < 200; i++) {
        keys.push('key#' + i)
        pids.push(i + 200000)
    }
    js = {
        keys: keys,
        pids: pids
    }

    start = process.hrtime()
    for (var i = 0; i < n; i++) {
        data = JSON.stringify(js)
    }
    end = process.hrtime(start)
    console.log('json save = %s, size = %d', (end[0] + end[1] * 1e-9), data.length)

    start = process.hrtime()
    for (var i = 0; i < n; i++) {
        js = JSON.parse(data)
    }
    end = process.hrtime(start)
    console.log('json save = %s, size = %d', end[0] + end[1] * 1e-9, data.length)
}

n = 10000
json_bench(n)
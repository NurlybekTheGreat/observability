function replace_backslash(tag, timestamp, record)
    local container_name = record["container_name"]
    if container_name then
        record["container_name"] = string.gsub(container_name, "\\", "a")
    end
    return 1, timestamp, record
end

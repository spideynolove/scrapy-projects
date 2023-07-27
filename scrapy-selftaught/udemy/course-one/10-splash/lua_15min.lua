-------------------------------------------------------------
-- https://tylerneylon.com/a/learn-lua/
-- https://www.tutorialspoint.com/lua/lua_variables.htm
-------------------------------------------------------------

local num_one = 42

local s = 'walternate' -- Immutable strings like Python.
local t = "double-quotes are also fine"
local u = [[ Double brackets
       start and end
       multi-line strings.]]
local t = nil


while num_one < 50 do
    num_one = num_one + 1 -- No ++ or += type operators.
    print(num_one)
end


local num = 42

if num > 40 then
    print('over 40')
elseif s ~= 'walternate' then -- ~= is not equals.
    -- Equality check is == like Python; ok for strs.
    io.write('not over 40\n') -- Defaults to stdout.
else
    -- Variables are global by default.
    local thisIsGlobal = 5 -- Camel case is common.

    -- How to make a variable local:
    local line = io.read() -- Reads next stdin line.

    -- String concatenation uses the .. operator:
    print('Winter is coming, ' .. line)
end


-- foo = anUnknownVariable
local aBoolValue = false

if not aBoolValue then print('twas false') end

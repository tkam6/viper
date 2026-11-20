#!/usr/bin/zsh
zmodload zsh/datetime
get_time() {
    date "+%d-%m-%Y %H:%M:%S"
}
echo "starting test generation at $(get_time)"
start_gen=$EPOCHREALTIME
dir=$(./generate_fuzzy_inp.py 1000 10000000)
end_gen=$EPOCHREALTIME
printf "test generation done; took %.3fs\n" "$((end_gen - start_gen))"
echo "starting tests at $(get_time)"
start_test=$EPOCHREALTIME
./test_fuzzy.py "$dir" >/dev/null
end_test=$EPOCHREALTIME
printf "done testing in %.3fs at %s\n" "$((end_test - start_test))" "$(get_time)"

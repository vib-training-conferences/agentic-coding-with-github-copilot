/**
 * Solution 2.3: Translation of Python sequence utilities to C++17
 *
 * Compile with:
 *   g++ -std=c++17 -O2 -o sequence_utils 03_translate_script.cpp
 *
 * Run with:
 *   ./sequence_utils
 */

#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

/**
 * @brief Calculate the GC content of a DNA sequence as a percentage.
 *
 * @param sequence DNA sequence string (A, T, G, C; case-insensitive).
 * @return GC content as a percentage (0.0 – 100.0).
 * @throws std::invalid_argument if the sequence contains non-DNA characters.
 */
double calculate_gc_content(const std::string& sequence) {
    if (sequence.empty()) {
        return 0.0;
    }

    std::string upper_seq = sequence;
    std::transform(upper_seq.begin(), upper_seq.end(), upper_seq.begin(), ::toupper);

    for (char c : upper_seq) {
        if (c != 'A' && c != 'C' && c != 'G' && c != 'T') {
            throw std::invalid_argument("Invalid nucleotide in sequence: " + sequence);
        }
    }

    int gc_count = 0;
    for (char c : upper_seq) {
        if (c == 'G' || c == 'C') {
            ++gc_count;
        }
    }
    return (static_cast<double>(gc_count) / static_cast<double>(upper_seq.size())) * 100.0;
}

/**
 * @brief Convert a DNA sequence to its RNA equivalent.
 *
 * Replaces thymine (T/t) with uracil (U/u), preserving original case.
 *
 * @param sequence DNA sequence string.
 * @return RNA sequence string.
 * @throws std::invalid_argument if the sequence contains non-DNA characters.
 */
std::string transcribe_dna_to_rna(const std::string& sequence) {
    std::string upper_seq = sequence;
    std::transform(upper_seq.begin(), upper_seq.end(), upper_seq.begin(), ::toupper);

    for (char c : upper_seq) {
        if (c != 'A' && c != 'C' && c != 'G' && c != 'T') {
            throw std::invalid_argument("Invalid nucleotide in sequence: " + sequence);
        }
    }

    std::string result = sequence;
    for (char& c : result) {
        if (c == 'T') c = 'U';
        else if (c == 't') c = 'u';
    }
    return result;
}

/**
 * @brief Return the reverse complement of a DNA sequence (uppercase output).
 *
 * @param sequence DNA sequence string (case-insensitive).
 * @return Reverse complement as an uppercase string.
 * @throws std::invalid_argument if the sequence contains non-DNA characters.
 */
std::string reverse_complement(const std::string& sequence) {
    std::string upper_seq = sequence;
    std::transform(upper_seq.begin(), upper_seq.end(), upper_seq.begin(), ::toupper);

    for (char c : upper_seq) {
        if (c != 'A' && c != 'C' && c != 'G' && c != 'T') {
            throw std::invalid_argument("Invalid nucleotide in sequence: " + sequence);
        }
    }

    std::string result;
    result.reserve(upper_seq.size());

    const std::map<char, char> complement = {{'A', 'T'}, {'T', 'A'}, {'G', 'C'}, {'C', 'G'}};
    for (auto it = upper_seq.rbegin(); it != upper_seq.rend(); ++it) {
        result += complement.at(*it);
    }
    return result;
}

/**
 * @brief Calculate the melting temperature (Tm) of a DNA primer.
 *
 * Uses the Wallace rule for primers up to 13 bp:
 *   Tm = 2*(A+T) + 4*(G+C)
 *
 * Uses a simplified nearest-neighbour approximation for longer primers:
 *   Tm = 81.5 + 16.6*log10([Na+]) + 0.41*%GC - 675/n
 * with [Na+] = 0.05 M.
 *
 * @param sequence DNA primer sequence (case-insensitive).
 * @return Melting temperature in degrees Celsius, rounded to 2 decimal places.
 */
double calculate_melting_temperature(const std::string& sequence) {
    std::string upper_seq = sequence;
    std::transform(upper_seq.begin(), upper_seq.end(), upper_seq.begin(), ::toupper);

    int n = static_cast<int>(upper_seq.size());
    int gc_count = 0;
    int at_count = 0;
    for (char c : upper_seq) {
        if (c == 'G' || c == 'C') ++gc_count;
        else if (c == 'A' || c == 'T') ++at_count;
    }

    double tm;
    if (n <= 13) {
        tm = 2.0 * at_count + 4.0 * gc_count;
    } else {
        double gc_percent = (static_cast<double>(gc_count) / n) * 100.0;
        double sodium_concentration = 0.05;
        tm = 81.5 + 16.6 * std::log10(sodium_concentration) + 0.41 * gc_percent - 675.0 / n;
    }

    // Round to 2 decimal places
    return std::round(tm * 100.0) / 100.0;
}

/**
 * @brief Find restriction enzyme recognition sites in a DNA sequence.
 *
 * @param sequence DNA sequence to search (case-insensitive).
 * @param enzyme_sites Map from enzyme name to recognition sequence.
 * @return Vector of (enzyme_name, position) pairs sorted by position.
 *         Positions are 0-indexed.
 */
std::vector<std::pair<std::string, std::size_t>>
find_restriction_sites(const std::string& sequence,
                        const std::map<std::string, std::string>& enzyme_sites) {
    std::string upper_seq = sequence;
    std::transform(upper_seq.begin(), upper_seq.end(), upper_seq.begin(), ::toupper);

    std::vector<std::pair<std::string, std::size_t>> results;

    for (const auto& [enzyme, site] : enzyme_sites) {
        std::string upper_site = site;
        std::transform(upper_site.begin(), upper_site.end(), upper_site.begin(), ::toupper);

        std::size_t pos = 0;
        while ((pos = upper_seq.find(upper_site, pos)) != std::string::npos) {
            results.emplace_back(enzyme, pos);
            ++pos;
        }
    }

    std::sort(results.begin(), results.end(),
              [](const auto& a, const auto& b) { return a.second < b.second; });

    return results;
}

// ── main ─────────────────────────────────────────────────────────────────────

int main() {
    const std::string test_sequence =
        "ATGCGAATTCGGATCCATGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG";

    std::cout << "=== Sequence Analysis ===" << std::endl;
    std::cout << "Sequence: " << test_sequence << std::endl;
    std::cout << "GC content: " << calculate_gc_content(test_sequence) << "%" << std::endl;
    std::cout << "RNA transcript: " << transcribe_dna_to_rna(test_sequence) << std::endl;
    std::cout << "Reverse complement: " << reverse_complement(test_sequence) << std::endl;
    std::cout << "Melting temperature: " << calculate_melting_temperature(test_sequence)
              << " C" << std::endl;

    std::map<std::string, std::string> enzyme_sites = {
        {"EcoRI",   "GAATTC"},
        {"BamHI",   "GGATCC"},
        {"HindIII", "AAGCTT"},
    };

    auto sites = find_restriction_sites(test_sequence, enzyme_sites);
    std::cout << "\nRestriction sites found:" << std::endl;
    for (const auto& [enzyme, pos] : sites) {
        std::cout << "  " << enzyme << " at position " << pos << std::endl;
    }

    return 0;
}
